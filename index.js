/*const litra = require("litra");

const device = litra.findDevice();

let timeoutId

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

    /*let intervalId = setInterval(() => grad(), 7500)

}


function grad() {
    //console.log("AH")
    for(let i = 1; i <= 25; i++) { 
        timeoutId = setTimeout(() => litra.setRGBColor(device, i*10, (i-1)*10, (i-1)*10), 100*i)

        setTimeout(() => litra.setRGBColor(device, 0, i*10, 0), 100*i + 2500)

        setTimeout(() => litra.setRGBColor(device, 0, 0, i*10), 100*i + 5000)
    }
    clearTimeout(timeoutId)
     

}*/


const litra = require("litra");

const device = litra.findDevice();

if (device) {
    litra.setZoneColorRGB(device, 1, 0, 0, 0);
    litra.setZoneColorRGB(device, 2, 0, 0, 0);
    litra.setZoneColorRGB(device, 3, 0, 0, 0);
    litra.setZoneColorRGB(device, 4, 0, 0, 255);
    litra.setZoneColorRGB(device, 5, 0, 0, 0);
    litra.setZoneColorRGB(device, 6, 0, 0, 0);
    litra.setZoneColorRGB(device, 7, 0, 0, 0);
}

  