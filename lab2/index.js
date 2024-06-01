const { exec } = require('child_process'); 
 
function getDiskInfo() { 
    exec('wmic logicaldisk get Caption, DriveType, Size, FreeSpace', (err, stdout) => { 
        if (err) { 
            console.error(err); 
            return; 
        } 
         
        const lines = stdout.trim().split('\r\n'); 
        const diskInfo = lines.slice(1, lines.length - 1).map(line => { 
            const [letter, type, size, freeSpace] = line.trim().split(/\s+/); 
            return { 
                letter, 
                type: type === '3' ? 'Local Disk' : type === '2' ? 'USB Drive' : 'Unknown', 
                size: parseInt(size), 
                freeSpace: parseInt(freeSpace) 
            }; 
        }); 
         
        console.log('Disk Info:'); 
        diskInfo.forEach(disk => { 
            console.log(`${disk.letter} - ${disk.type} - ${disk.size} - ${disk.freeSpace}`); 
        }); 
         
        setInterval(() => { 
            diskInfo.forEach(disk => { 
                console.log(`Free space on ${disk.letter}: ${disk.freeSpace}`); 
            }); 
        }, 5000); 
    }); 
} 
 
function getUSBInfo() { 
    exec('wmic logicaldisk where DriveType=2 get Caption', (err, stdout) => { 
        if (err) { 
            console.error(err); 
            return; 
        } 
        const lines = stdout.trim().split('\r\n'); 
        const usbInfo = lines.slice(1, lines.length - 1).map(line => line.trim()); 
        console.log('USB Drives connected:'); 
        console.log(usbInfo.join('\n')); 
    }); 
} 
 
getDiskInfo(); 
getUSBInfo();