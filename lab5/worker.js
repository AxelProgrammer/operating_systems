
self.onmessage = function(event) {
    // Пример обработки сообщения
    const messageFromMainThread = event.data;
    self.postMessage('Message from worker: ' + messageFromMainThread.toUpperCase());
  };
  