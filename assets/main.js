const toggle=document.querySelector('.menu-toggle');const nav=document.querySelector('#main-nav');
toggle?.addEventListener('click',()=>{const expanded=toggle.getAttribute('aria-expanded')==='true';toggle.setAttribute('aria-expanded',String(!expanded));nav.classList.toggle('open',!expanded)});
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&nav?.classList.contains('open')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.focus()}});
nav?.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{nav.classList.remove('open');toggle?.setAttribute('aria-expanded','false')}));

// Show one class at a time, starting with the selected graduating class.
const tabs=[...document.querySelectorAll('[data-year]')];
function selectYear(tab,focus=false){tabs.forEach(t=>t.setAttribute('aria-pressed',String(t===tab)));document.querySelectorAll('.placement-panel').forEach(panel=>{panel.hidden=panel.id!==`class-${tab.dataset.year}`});if(focus)tab.focus()}
tabs.forEach((tab,index)=>{tab.addEventListener('click',()=>selectYear(tab));tab.addEventListener('keydown',event=>{let next;if(event.key==='ArrowRight')next=(index+1)%tabs.length;if(event.key==='ArrowLeft')next=(index+tabs.length-1)%tabs.length;if(event.key==='Home')next=0;if(event.key==='End')next=tabs.length-1;if(next!==undefined){event.preventDefault();selectYear(tabs[next],true)}})});
if(tabs.length)selectYear(tabs.find(tab=>tab.getAttribute('aria-pressed')==='true')||tabs[0]);

const reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
const gallery=document.querySelector('.gallery-track');
function scrollGallery(direction){gallery?.scrollBy({left:direction*(gallery.querySelector('button').getBoundingClientRect().width+24),behavior:reducedMotion.matches?'instant':'smooth'})}
document.querySelector('[data-gallery-prev]')?.addEventListener('click',()=>scrollGallery(-1));
document.querySelector('[data-gallery-next]')?.addEventListener('click',()=>scrollGallery(1));
gallery?.addEventListener('keydown',event=>{if(event.target===gallery&&['ArrowLeft','ArrowRight'].includes(event.key)){event.preventDefault();scrollGallery(event.key==='ArrowLeft'?-1:1)}});

const photos=[...document.querySelectorAll('[data-photo]')];const lightbox=document.querySelector('.lightbox');let currentPhoto=0;
function showPhoto(index){currentPhoto=(index+photos.length)%photos.length;const photo=photos[currentPhoto];lightbox.querySelector('img').src=photo.dataset.photo;lightbox.querySelector('img').alt=photo.querySelector('img').alt;lightbox.querySelector('p').textContent=photo.dataset.caption}
photos.forEach((photo,index)=>photo.addEventListener('click',()=>{showPhoto(index);lightbox.showModal();document.body.style.overflow='hidden'}));
document.querySelector('.lightbox-close')?.addEventListener('click',()=>lightbox.close());
lightbox?.addEventListener('close',()=>{document.body.style.overflow='';photos[currentPhoto]?.focus()});
lightbox?.addEventListener('click',event=>{if(event.target===lightbox){const rect=lightbox.getBoundingClientRect();if(event.clientX<rect.left||event.clientX>rect.right||event.clientY<rect.top||event.clientY>rect.bottom)lightbox.close()}});
lightbox?.addEventListener('keydown',event=>{if(event.key==='ArrowRight'){event.preventDefault();showPhoto(currentPhoto+1)}if(event.key==='ArrowLeft'){event.preventDefault();showPhoto(currentPhoto-1)}});
document.querySelector('[data-lightbox-prev]')?.addEventListener('click',()=>showPhoto(currentPhoto-1));
document.querySelector('[data-lightbox-next]')?.addEventListener('click',()=>showPhoto(currentPhoto+1));

// Reveal only below-the-fold content; everything remains visible without JavaScript.
if('IntersectionObserver' in window&&!reducedMotion.matches){const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}),{threshold:.08});document.querySelectorAll('.reveal').forEach(item=>{if(item.getBoundingClientRect().top>window.innerHeight){item.classList.add('will-reveal');observer.observe(item)}})}
