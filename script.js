const wsUri = "ws://localhost:8008";
const socket = new WebSocket(wsUri);
console.log('agga')
socket.addEventListener("open", (event) => {
    console.log('shit opened'),
    socket.send("Hello Server!");
});
socket.addEventListener("message", (event) => {
  console.log("Message from server ", event.data);
  socket.send("fuckyou!");
});
socket.addEventListener("close", (event) => {
    console.log('fucj');
});