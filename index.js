const litra = require("litra");

const device = litra.findDevice();

let timeoutId

const ACTION = {
    MOTIVATE: 0,
    WAKE_UP: 1,
    SOOTH: 2,
    ANGER: 3
}


// Turn your light on, then turn it off again after 5 seconds
if (device) {
    //litra.setRGBColor(device, 1, 0, 0);
    //litra.setBrightnessPercentage(device, 10);

    //setTimeout(() => litra.setRGBColor(device, 255, 0, 0), 0)
    //setTimeout(() => litra.setRGBColor(device, 0, 255, 0), 500)
    //setTimeout(() => litra.setRGBColor(device, 0, 0, 255), 1000)

    /*for(let i = 0; i < 25; i++) { 
        setTimeout(() => litra.setRGBColor(device, i*10, 0, 0), 100*i)
        setTimeout(() => litra.setRGBColor(device, 0, i*10, 0), 100*i + 2500)
        setTimeout(() => litra.setRGBColor(device, 0, 0, i*10), 100*i + 5000)
    }*/

    //let intervalId = setInterval(() => wake_up(), 7*70*2)
    //grad()
    //tell_light_to(ACTION.SOOTH)
    AHHH()

}


function grad() {
    //console.log("AH")
    /*for(let t = 0; t <= 25; t++) { 
        for(let i = 1; i <= 7; i++) { 
            let timeoutId = setTimeout(() => litra.setZoneColorRGB(device, i, 0, 0, (((t*10)*(i/7)) % 250 )), t*10 + i*100);
        }
        //clearTimeout(timeoutId)
    }*/
    for(let i = 1; i <= 7; i++) { 
        let timeoutId = setTimeout(() => litra.setZoneColorRGB(device, i, i * 209 / 7, i * 170 / 7, i * 255 / 7 ), i*100);
        setTimeout(() => litra.setZoneColorRGB(device, 8-i, i * 209 / 7, i * 170 / 7, i * 255 / 7 ), i*100 + 700);
        //setTimeout(() => litra.setZoneColorRGB(device, i, 0, i * 170 / 7, 0), i*100 + 700);
        //setTimeout(() => litra.setZoneColorRGB(device, i, 0, 0, i * 255 / 7 ), i*100 + 1400);
    }
    clearTimeout(timeoutId)
     
}

function AHHH() {
    for(let i = 1; i <= 10; i+=2) {
        let timeoutId = setTimeout(() => tell_light_to(ACTION.ANGER), (i+1)*100)
        setTimeout(() => tell_light_to(), i*100)
    }
}


function tell_light_to(action) {
    switch(action) {
        case ACTION.MOTIVATE: setLightMood(241, 194, 50); break;
        case ACTION.WAKE_UP: setLightMood(41, 134, 204); break;
        case ACTION.SOOTH: setLightMood(188, 139, 145); break;
        case ACTION.ANGER: setLightMood(0, 0, 255); break;
        default: setLightMood(255, 255, 255)
    }
}

function setLightMood(R, G ,B) {
    litra.setRGBColor(device, R, G, B)
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


  