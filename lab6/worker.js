let priority = 'normal';
let counter = 0;

self.addEventListener('message', function(e) {
    const data = e.data;

    switch (data.type) {
        case 'increment':
            counter++;
            self.postMessage(counter);
            break;
        case 'changePriority':
            changePriority();
            break;
        default:
            console.error('Unknown message type');
    }
});

function changePriority() {
    priority = priority === 'normal' ? 'high' : 'normal';
    self.postMessage('Priority changed to ' + priority);
}
