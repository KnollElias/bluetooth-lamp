const noble = require("noble");

noble.on("stateChange", (state) => {
  if (state === "poweredOn") {
    console.log("Scanning for Bluetooth devices...");
    noble.startScanning();
  } else {
    noble.stopScanning();
  }
});

noble.on("discover", (device) => {
  console.log(`Found device: ${device.advertisement.localName}`);
  console.log(`  Device ID: ${device.id}`);
  console.log(`  Device Address: ${device.address}`);
});
