const litra = require("litra");

const device = litra.findDevice();

let timeoutId

const ACTION = {
    MOTIVATE: 0,
    WAKE_UP: 1,
    SOOTH: 2,
    ANGER: 3
}

if(device) {
    wake_up_fade()
}

function wake_up_fade() {
    const R = 41
    const G = 134
    const B = 204
    for(let T = 0; T < 7; T++) { 
        for(let i = 1; i <= 7; i++) { 
            const ratio = ((i/7) + 0.5)/1.5
            let timeoutId = setTimeout(() => litra.setZoneColorRGB(device, (i+T) % 7 + 1, ratio * R, ratio*G, ratio*B), (i*10 + T*70)*2);
            //setTimeout(() => litra.setZoneColorRGB(device, 8-i, i * 209 / 7, i * 170 / 7, i * 255 / 7 ), i*100 + 700);
            //setTimeout(() => litra.setZoneColorRGB(device, i, 0, i * 170 / 7, 0), i*100 + 700);
            //setTimeout(() => litra.setZoneColorRGB(device, i, 0, 0, i * 255 / 7 ), i*100 + 1400);
        }
    }

    clearTimeout(timeoutId)
}


  