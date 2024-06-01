const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');

let mainWindow;

app.on('ready', () => {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true // Разрешаем использование Node.js веб-модулей
    }
  });

  mainWindow.loadFile('index.html');

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
});

ipcMain.on('toggleThread', (event, { thread }) => {
  const worker = thread === 1 ? worker1 : worker2;
  sendMessageToWorker(worker, { action: 'start', thread: thread });
});

ipcMain.on('changePriority', () => {
  // Изменение приоритета (если нужно)
});

function sendMessageToWorker(worker, message) {
  worker.postMessage(message);
}
