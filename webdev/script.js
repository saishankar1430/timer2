const output = document.getElementById('output');
const minInput = document.getElementById('min');
const secInput = document.getElementById('sec');
const startBtn = document.getElementById('start');
const pauseBtn = document.getElementById('pause');
const resetBtn = document.getElementById('reset');
const presets = document.querySelectorAll('.preset');
const ring = document.getElementById('ring');

let totalSeconds = 25 * 60;
let remaining = totalSeconds;
let timerId = null;

function formatTime(s){
    const m = Math.floor(s/60).toString().padStart(2,'0');
    const sec = (s%60).toString().padStart(2,'0');
    return `${m}:${sec}`;
}

function render(){
    output.textContent = formatTime(remaining);
    const pct = 1 - (remaining / totalSeconds || 1);
    const deg = Math.max(0, Math.min(360, pct * 360));
    ring.style.background = `conic-gradient(var(--accent) ${deg}deg, #e6eefc ${deg}deg)`;
}

function start(){
    if (timerId) return;
    if (remaining <= 0) remaining = totalSeconds;
    timerId = setInterval(()=>{
        remaining--;
        render();
        if (remaining <= 0){
            clearInterval(timerId);
            timerId = null;
            notifyDone();
        }
    },1000);
}

function pause(){
    if (!timerId) return;
    clearInterval(timerId);
    timerId = null;
}

function reset(){
    pause();
    remaining = totalSeconds;
    render();
}

function notifyDone(){
    render();
    ring.style.boxShadow = '0 0 0 6px rgba(16,185,129,0.12), 0 10px 30px rgba(16,185,129,0.08)';
    try{ new Audio("https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg").play(); }catch(e){}
}

startBtn.addEventListener('click', ()=>{
    const m = Math.max(0, parseInt(minInput.value) || 0);
    const s = Math.max(0, parseInt(secInput.value) || 0);
    totalSeconds = m*60 + s || 25*60;
    remaining = totalSeconds;
    render();
    start();
});

pauseBtn.addEventListener('click', pause);
resetBtn.addEventListener('click', reset);

presets.forEach(btn=>{
    btn.addEventListener('click', ()=>{
        const m = parseInt(btn.dataset.min,10)||25;
        minInput.value = m;
        secInput.value = 0;
        totalSeconds = m*60;
        remaining = totalSeconds;
        render();
    });
});

// initialize UI
minInput.addEventListener('input', ()=>{
    const m = Math.max(0, parseInt(minInput.value) || 0);
    totalSeconds = m*60 + (parseInt(secInput.value)||0);
    remaining = totalSeconds;
    render();
});
secInput.addEventListener('input', ()=>{
    let s = Math.max(0, Math.min(59, parseInt(secInput.value)||0));
    secInput.value = s;
    totalSeconds = (parseInt(minInput.value)||0)*60 + s;
    remaining = totalSeconds;
    render();
});

render();
    