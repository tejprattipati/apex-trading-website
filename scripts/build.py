"""Build ATG's static pages. Python 3 standard library only; no runtime required."""
from pathlib import Path
from html import escape as e
import json

ROOT = Path(__file__).resolve().parents[1]
D = json.loads((ROOT / 'data/content.json').read_text())
INTEREST = D['links']['INTEREST FORM']
APPLICATION = D['links']['APPLICATION']
INSTAGRAM = D['links']['Instagram']
LOGO = D['branding']['preferred_white_wordmark']['file']
PAGES = [('index.html','Home'),('about.html','About'),('placement.html','Placement'),('prospective-members.html','Prospective members')]

def image(asset, alt, cls='', eager=False, extra=''):
    return f'<img src="{asset["file"]}" alt="{e(alt)}" class="{cls}" width="{asset.get("optimized_width",800)}" height="{asset.get("optimized_height",600)}" loading="{"eager" if eager else "lazy"}" {extra}>'

def ext(url, label, cls=''):
    return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener">{label}</a>'

def header(page):
    links=''.join(f'<a href="{path}"'+(' aria-current="page"' if path==page else '')+f'>{name}</a>' for path,name in PAGES)
    forms='' if page=='prospective-members.html' else ext(INTEREST,'Interest form ↗','nav-interest')+ext(APPLICATION,'Application ↗','button small')
    return f'''<a class="skip-link" href="#main">Skip to content</a><header class="site-header">
    <a class="brand" href="index.html" aria-label="Apex Trading Group home"><span class="brand-mark"><img src="{LOGO}" alt="ATG" width="{D['branding']['preferred_white_wordmark']['optimized_width']}" height="{D['branding']['preferred_white_wordmark']['optimized_height']}"></span><span class="brand-name">APEX<br>TRADING GROUP</span></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="main-nav">Menu <span aria-hidden="true">☰</span></button><nav id="main-nav" aria-label="Main navigation">{links}{forms}</nav></header>'''

def footer(page):
    actions=ext(INTEREST,'Stay in the loop <span>↗</span>','button')
    if page=='prospective-members.html':
        actions=f'''<div class="prospective-actions">{ext(APPLICATION,'<span>View the application</span><span aria-hidden="true">↗</span>','button')}{ext(INTEREST,'<span>Interest form</span><span aria-hidden="true">↗</span>','button')}</div>'''
    return f'''<section class="join-band"><div class="wrap join-inner"><div><p class="eyebrow light">Your next chapter</p><h2>Build your future.<br><em>Find your people.</em></h2></div><div><p>Curious about investing? Get to know ATG.</p>{actions}</div></div></section>
    <footer class="site-footer"><div class="wrap footer-main"><a class="footer-brand" href="index.html"><img src="{LOGO}" alt="Apex Trading Group" width="150" height="80"><span>Built by students, for students.<br>University of Michigan · Ann Arbor</span></a><div><p class="eyebrow light">Explore</p>{''.join(f'<a href="{path}">{name}</a>' for path,name in PAGES)}</div><div><p class="eyebrow light">Get in touch</p><a href="mailto:atgeboard26@umich.edu">atgeboard26@umich.edu</a>{ext(INSTAGRAM,'Instagram ↗')}{ext(INTEREST,'Interest form ↗')}{ext(APPLICATION,'Application ↗')}</div></div><div class="wrap footer-bottom"><span>© 2026 Apex Trading Group</span><span>Est. 2014 — Ann Arbor, MI</span><a href="#top">Back to top ↑</a></div></footer>'''

def stats():
    return '''<section id="at-a-glance" class="stats wrap" aria-label="ATG at a glance"><div><strong>60<span>+</span></strong><p>Active members</p></div><div><strong>120<span>+</span></strong><p>Alumni</p></div><div><strong>$25,000</strong><p>Assets under management</p></div><div><strong>100<span>%</span></strong><p>Full-time placement</p></div></section>'''

def pillars(full=False):
    descriptions=["Put your ideas to work. Research businesses, develop investment theses, and help manage ATG’s $25,000 student-run portfolio.","Learn from members who have been in your shoes, with structured support for recruiting, technical preparation, and career decisions.","Connect with a community that shares an interest in finance—and brings a wide range of backgrounds, hobbies, and experiences to Michigan."]
    cards=''
    for i,p in enumerate(D['pillars']):
        desc=p['source_description'].replace('$10k','$25,000').rstrip('.')+'.' if full else descriptions[i]
        cards+=f'''<article class="pillar reveal" id="pillar-{i+1}"><div class="pillar-photo">{image(p['photo'],['ATG members together at a club event','ATG members at a professional event','ATG members socializing'][i])}<span>0{i+1}</span></div><div class="pillar-copy"><p class="eyebrow">{['Invest','Develop','Belong'][i]}</p><h3>{e(p['title'])}</h3><p>{e(desc)}</p>{f'<a class="text-link" href="about.html#pillar-{i+1}">Discover more <span>↗</span></a>' if not full else ''}</div></article>'''
    return f'<div class="pillars">{cards}</div>'

def recruitment(show_interest=True):
    events=''
    for item in D['recruitment']['events']:
        date=item['date']; detail=item.get('location',item.get('time',''))
        if item.get('alternative_sublabel'): detail += ' · '+item['alternative_sublabel']
        events+=f'<li class="event"><time datetime="{date}"><span>SEP</span>{int(date[-2:]):02d}</time><div><h3>{e(item["title"])}</h3><p>{e(detail)}</p></div><span class="event-line" aria-hidden="true">—</span></li>'
    return f'''<section class="section recruitment" id="recruitment"><div class="wrap recruitment-layout"><div class="recruitment-intro"><p class="eyebrow">Fall 2026 / Recruitment</p><h2>It starts with<br><em>a conversation.</em></h2><p>Meet the members, explore the experience, and take the next step with ATG.</p>{ext(INTEREST,'Join the interest list <span>↗</span>','button dark') if show_interest else ''}<p class="schedule-note">Fall 2026 schedule · September 9–21<br>Follow our interest list for future updates.</p></div><ol class="event-list">{events}</ol></div></section>'''

def gallery():
    photos=''
    for i,p in enumerate(D['gallery']):
        focal=p.get('focal_point',[.5,.5]); pos=f'{focal[0]*100:.1f}% {focal[1]*100:.1f}%'
        photos+=f'''<button class="gallery-photo" data-photo="{p['file']}" data-caption="ATG community · Photo {i+1} of 12" aria-label="Open ATG community photo {i+1}">{image(p,f'ATG members at a club gathering, photo {i+1}',extra=f'style="object-position:{pos}"')}</button>'''
    return f'''<section class="section community-section"><div class="wrap section-heading"><div><p class="eyebrow light">Beyond the portfolio</p><h2>A shared interest.<br><em>A lasting community.</em></h2></div><div class="gallery-controls"><button class="round-button" data-gallery-prev aria-label="Previous club photos">←</button><button class="round-button" data-gallery-next aria-label="Next club photos">→</button></div></div><div class="gallery-track wrap" aria-label="ATG community photos" tabindex="0">{photos}</div><div class="wrap gallery-footer"><p>Moments from life at ATG</p>{ext(INSTAGRAM,'Follow @atgumich <span>↗</span>','text-link')}</div></section><dialog class="lightbox" aria-label="ATG community photo"><button class="lightbox-close" aria-label="Close photo">✕</button><img alt=""><p></p><div class="lightbox-controls"><button data-lightbox-prev aria-label="Previous photo">←</button><button data-lightbox-next aria-label="Next photo">→</button></div></dialog>'''

def logo_grid(home=False):
    logos=D['placement']['logos']
    available={logo['company']:logo for logo in logos+D['placement'].get('additional_logos',[])}
    if home:
        logos=[available[company] for company in D['placement']['home_featured_companies']]
    else:
        logos=[available.get(company,{'company':company}) for company in D['placement']['display_companies']]
    cards=''
    for logo in logos:
        company=e(logo['company'])
        extra='style="filter:brightness(0)"' if logo.get('asset',{}).get('monochrome') else ''
        mark=image(logo['asset'],logo['company'],extra=extra)+f'<span>{company}</span>' if logo.get('asset') else f'<strong class="firm-wordmark">{company}</strong>'
        cls=' firm-logo-wide' if logo.get('wide') else ''
        if logo.get('size'): cls+=' firm-logo-'+logo['size']
        cards+=f'<div class="firm-logo{cls}" title="{company}">{mark}</div>'
    return '<div class="logo-grid'+(' home-logos' if home else '')+'">'+cards+'</div>'

def broader_placements():
    companies=D['placement'].get('broader_careers',[])
    if not companies:return ''
    firms=''.join(f'<li>{e(company)}</li>' for company in companies)
    return f'''<section class="section wrap broader-careers"><div class="section-heading"><div><p class="eyebrow">Beyond financial services</p><h2>Different paths.<br><em>Shared foundations.</em></h2></div><p class="section-aside">Our alumni have also built careers across technology, consulting, industry, and entrepreneurship.</p></div><ul class="career-firms">{firms}</ul></section>'''

def subhero(kicker,heading,copy,photo=None,caption=''):
    if photo:
        return f'''<section class="subhero photo-subhero"><div class="wrap subhero-grid"><div><p class="eyebrow light">{kicker}</p><h1>{heading}</h1><p class="lead">{copy}</p></div><figure>{image(photo,caption or 'Apex Trading Group members',eager=True)}{f'<figcaption>{caption}</figcaption>' if caption else ''}</figure></div></section>'''
    return f'''<section class="subhero"><div class="subhero-sky"></div><div class="wrap"><p class="eyebrow light">{kicker}</p><h1>{heading}</h1><p class="lead">{copy}</p></div></section>'''

def home():
    return f'''<section class="hero"><img class="hero-image" src="assets/images/manhattan-blue-hour.jpg" alt="Lower Manhattan and One World Trade Center at blue hour" fetchpriority="high" width="2600" height="1733"><div class="hero-shade"></div><div class="hero-content wrap"><p class="eyebrow light">University of Michigan <span>Est. 2014</span></p><h1>Invest in markets.<br><em>Grow together.</em></h1><p class="hero-intro">Apex Trading Group brings Michigan students together to turn curiosity into conviction—through hands-on investing, shared ambition, and a community that lasts.</p><div class="actions"><a class="button" href="prospective-members.html">The ATG experience <span>↗</span></a><a class="text-link" href="about.html">Get to know us <span>→</span></a></div></div><div class="hero-bottom wrap"><span>The premier student investment organization<br>at the Ross School of Business</span><a href="#at-a-glance">Explore ATG <span>↓</span></a></div></section>{stats()}
    <section class="section wrap story"><div class="story-heading reveal"><p class="eyebrow">01 / Our story</p><h2>Built by students.<br><em>For students.</em></h2><a class="text-link" href="about.html">Meet Apex Trading Group <span>↗</span></a></div><div class="story-copy reveal"><p class="story-lead">An education in the markets.<br>A community for everything after.</p><p>Founded in 2014, Apex Trading Group is a student-run investment organization at the University of Michigan’s Ross School of Business. Through hands-on portfolio management, equity research, and stock pitches, our members turn classroom learning into real investing experience.</p><p>We learn from one another, challenge each other’s ideas, and support each other’s growth. That shared commitment prepares our members for careers in finance and beyond—and builds connections that last well past Michigan.</p></div></section>
    <section class="section pillars-section"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">02 / Our pillars</p><h2>More than <em>investing.</em></h2></div><p class="section-aside">Three pillars. One shared commitment<br>to helping each other grow.</p></div>{pillars()}</div></section>
    {gallery()}
    <section class="section wrap"><div class="section-heading"><div><p class="eyebrow">03 / Where we go</p><h2>From Michigan.<br><em>To what’s next.</em></h2></div><a class="text-link" href="placement.html">Explore our placement <span>↗</span></a></div>{logo_grid(True)}</section>
    {recruitment()}'''

def people(entries):
    cards=''
    for person in entries:
        email=person.get('email')
        cards+=f'''<article class="person reveal"><div class="person-photo">{image(person['photo'],person['name'])}</div><div class="person-info"><p>{e(person['role'])}</p><h3>{e(person['name'])}</h3>{f'<a href="mailto:{email}">{email} <span>↗</span></a>' if email else ''}</div></article>'''
    return f'<div class="people-grid">{cards}</div>'

def about():
    leaders=D['chairs_and_sector_heads']
    sectors=[p for p in leaders if 'Sector Head' in p['role']]
    sectors.sort(key=lambda p: {'Tej Prattipati':0,'Christian Gojcaj':1,'Eddie Chen':2}.get(p['name'],3))
    chairs=[p for p in leaders if 'Sector Head' not in p['role'] and 'Chair' in p['role']]
    chairs.sort(key=lambda p: {'Shivam Shah':0,'Matthew Walsh-Hussey':1,'Matthew Hunt':2}.get(p['name'],3))
    advisors=[p for p in leaders if 'Advisor' in p['role']]
    return subhero('About Apex Trading Group','Shared ambition.<br><em>Individual potential.</em>','The University of Michigan’s premier student investment organization. Built around real-world experience, professional growth, and the people who make it possible.')+f'''
    <nav class="section-nav wrap" aria-label="About sections"><a href="#executive-board">Executive board ↓</a><a href="#sector-heads">Sector heads ↓</a><a href="#chairs">Chairs ↓</a><a href="#advisor">Senior advisor ↓</a><a href="#pillars">Our pillars ↓</a></nav>
    <section id="executive-board" class="section wrap"><div class="section-heading"><div><p class="eyebrow">The people behind ATG</p><h2>Executive <em>board.</em></h2></div><p class="section-aside">Students leading students.<br>Meet our executive team.</p></div>{people(D['board'])}</section>
    <section id="sector-heads" class="section chairs-section"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">Leading our investment teams</p><h2>Sector <em>heads.</em></h2></div></div>{people(sectors)}</div></section>
    <section id="chairs" class="section wrap"><div class="section-heading"><div><p class="eyebrow">Supporting our community</p><h2>Our <em>chairs.</em></h2></div></div>{people(chairs)}</section>
    <section id="advisor" class="section chairs-section"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">Experience & perspective</p><h2>Senior <em>advisor.</em></h2></div></div>{people(advisors)}</div></section>
    <section id="pillars" class="section wrap"><div class="section-heading"><div><p class="eyebrow">Our foundation</p><h2>The ATG <em>pillars.</em></h2></div></div>{pillars(True)}</section>'''

def placement():
    tabs='<div class="year-tabs" role="group" aria-label="Filter placement by class year"><button type="button" aria-pressed="true" data-year="all">All classes</button>'
    panels=''
    for year,entries in D['placement']['recent'].items():
        tabs+=f'<button type="button" aria-controls="class-{year}" aria-pressed="false" data-year="{year}" aria-label="Class of {year}">{year}</button>'
        panels+=f'<section class="placement-panel" id="class-{year}" aria-labelledby="class-title-{year}"><h3 id="class-title-{year}">Class of {year}</h3><ul>'+''.join(f'<li><span>{e(entry)}</span><span class="placement-dash" aria-hidden="true">—</span></li>' for entry in entries)+'</ul></section>'
    tabs+='</div>'
    return subhero('Placement / Our alumni network','Ambition meets<br><em>opportunity.</em>','Our members go on to work at leading firms in finance and beyond. An enduring alumni network connects every new class with the experience of those who came before.',D['placement']['club_photo'],'')+f'''
    {stats()}<section class="section wrap"><div class="section-heading"><div><p class="eyebrow">A network that stays with you</p><h2>Where our members<br><em>make their mark.</em></h2></div><p class="section-aside">Our members and alumni have worked across investment banking, investing, and financial services. Explore current and past roles across our network.</p></div>{logo_grid()}</section>{broader_placements()}
    <section class="section recent-section" id="recent-placement"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">Recent placement</p><h2>Every class.<br><em>New possibilities.</em></h2></div><p class="section-aside">Explore the firms and roles<br>of our recent classes.</p></div>{tabs}{panels}</div></section>'''

def pitch_highlights():
    entries=D['prospective_members'].get('pitch_highlights',[])
    if not entries:return ''
    rows=''
    for p in entries:
        gain=(p['closing_price']/p['pitch_price']-1)*100
        rows+=f'''<article class="pitch-result"><div><p class="pitch-ticker">{e(p['ticker'])} <span>· {e(p['pitch_term'])}</span></p><h4>{e(p['company'])}</h4></div><div><strong>{gain:+.1f}%</strong><p>Price return since pitch</p></div></article>'''
    return f'''<div class="pitch-highlights"><p class="eyebrow">Selected pitch highlights</p>{rows}<p class="returns-date">Returns as of September 2026</p></div>'''

def prospective():
    experiences=''
    for i,item in enumerate(D['prospective_members']['experiences']):
        text=item['description'].replace('cold- emailing','cold emailing').replace('bank- specific','bank-specific')
        extra=pitch_highlights() if item['title']=='Pitches' else ('<a class="text-link sector-jump" href="#investment-sectors">Explore our sectors <span>↓</span></a>' if item['title']=='Sector Teams' else '')
        experiences+=f'<details class="experience-row"'+(' open' if i==0 else '')+f'><summary><span>0{i+1}</span><h3>{e(item["title"])}</h3><span class="disclosure" aria-hidden="true">+</span></summary><p>{e(text)}.</p>{extra}</details>'
    sectors=''.join(f'<article class="sector-card"><div class="sector-card-image">{image(s["image"],s["alt"])}<span>0{i+1}</span></div><h3>{e(s["name"])}</h3></article>' for i,s in enumerate(D['prospective_members']['sector_cards']))
    return subhero('Prospective members','Your curiosity.<br><em>Our collective edge.</em>','The ATG experience connects practical investing, personal mentorship, and a community ready to grow with you.')+f'''
    <section class="section wrap experience-layout"><div><p class="eyebrow">The ATG experience</p><h2>Learn by doing.<br><em>Grow with others.</em></h2><p class="lead">From your first stock pitch to your next interview, build the skills and relationships that move you forward.</p></div><div class="experience-list"><p class="eyebrow">New member experience</p>{experiences}</div></section>
    <section class="section sector-grid-section" id="investment-sectors"><div class="wrap sector-grid-layout"><div class="sector-grid-intro"><p class="eyebrow light">Sector teams</p><h2>Our investment<br><em>sectors.</em></h2><p>Six investment desks. Members develop investment pitches and present them to our 60-person club. The Investment Committee votes on which ideas to add to ATG’s $25,000 long/short equity fund.</p></div><div class="sector-card-grid">{sectors}</div></div></section>
    {recruitment(show_interest=False)}'''

DESCRIPTIONS={
 'index.html':'Built by students, for students. Apex Trading Group is a student investment organization at the University of Michigan’s Ross School of Business.',
 'about.html':'Meet the executive board, chairs, and sector heads of Apex Trading Group at the University of Michigan.',
 'placement.html':'Explore Apex Trading Group’s alumni network, firm placements, and recent placement for the classes of 2026, 2027, and 2028.',
 'prospective-members.html':'Discover the ATG new member experience, six investment sectors, and Fall 2026 recruitment schedule.'}

def document(page,title,content):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0b1d33"><title>{title} — Apex Trading Group | University of Michigan</title><meta name="description" content="{e(DESCRIPTIONS.get(page,DESCRIPTIONS['index.html']))}"><link rel="icon" href="assets/images/atg-logo.png"><link rel="stylesheet" href="assets/fonts/fonts.css"><link rel="stylesheet" href="assets/style.css"></head><body id="top">{header(page)}<main id="main">{content}</main>{footer(page)}<script src="assets/main.js" defer></script></body></html>'''

for path,title,render in [('index.html','Home',home),('about.html','About',about),('placement.html','Placement',placement),('prospective-members.html','Prospective Members',prospective)]:
    (ROOT/path).write_text(document(path,title,render()))

# Preserve the original Wix slugs on both project and custom-domain Pages sites.
for alias,target in [('team-1','about.html'),('about','about.html'),('placement','placement.html'),('prospective-members','prospective-members.html')]:
    folder=ROOT/alias;folder.mkdir(exist_ok=True)
    text=(ROOT/target).read_text().replace('<head>','<head><base href="../">',1).replace('href="#',f'href="{target}#')
    (folder/'index.html').write_text(text)
(ROOT/'team-1.html').write_text((ROOT/'about.html').read_text())
(ROOT/'.nojekyll').touch()
notfound=document('404.html','Page not found','<section class="subhero"><div class="wrap"><p class="eyebrow light">404 / Page not found</p><h1>Let’s get you<br><em>back on track.</em></h1><div class="actions"><a class="button" href="index.html">Return home →</a></div></div></section>')
notfound=notfound.replace('<head>','<head><base href="https://tejprattipati.github.io/apex-trading-website/">',1).replace('href="#','href="index.html#')
(ROOT/'404.html').write_text(notfound)
print('Built four pages, legacy URL aliases, and 404 page.')
