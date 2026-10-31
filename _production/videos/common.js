
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const p=(t,a,b)=>cl((t-a)/(b-a));
const ease=x=>1-Math.pow(1-x,3);
const vis=(t,a,b,f=.5)=>Math.min(ease(p(t,a,a+f)),1-ease(p(t,b-f,b)));
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
function captions(t,caps){const c=caps.find(x=>t>=x[0]&&t<x[1]);const cap=$('#cap');
  if(c){cap.textContent=c[2];cap.style.opacity=Math.min(ease(p(t,c[0],c[0]+.4)),1-ease(p(t,c[1]-.3,c[1])));}else cap.style.opacity=0;}
function count(el,t,a,b){const to=+el.dataset.to,k=ease(p(t,a,b));el.textContent=(Math.round(to*k*10)/10).toString().replace(/\.0$/,'')+(el.dataset.suffix||'');}
const T=parseFloat((location.hash||'#0').slice(1))||0;
const io=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
// pan(img, t, a, b, [x,y,w] from, [x,y,w] to): show image region of width w (image px) at (x,y), eased from a to b
function pan(img,t,a,b,f,to,vw=920){const k=io(p(t,a,b));const x=f[0]+(to[0]-f[0])*k,y=f[1]+(to[1]-f[1])*k,w=f[2]+(to[2]-f[2])*k;const s=vw/w;img.style.transform=`translate(${-x*s}px,${-y*s}px) scale(${s})`;}
function typeLines(sel,t,a,step){$$(sel+' .ln').forEach((l,i)=>l.style.opacity=ease(p(t,a+i*step,a+i*step+.25)));}
