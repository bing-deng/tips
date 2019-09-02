* https://websockets.readthedocs.io/en/stable/intro.html#basic-example

  
  
  * 服务器接收
  ```
  var ws = new WebSocket("ws://127.0.0.1:5678/");


setInterval(function(){
    var rsi =$('span.pane-legend-item-value.pane-legend-line')[12]
    console.log(rsi.textContent)
    ws.send(rsi.textContent)
}, 3000);


  ```
  
  
  * 浏览器发送
  
  ```
  var ws = new WebSocket("ws://127.0.0.1:5678/");


setInterval(function(){
    var rsi =$('span.pane-legend-item-value.pane-legend-line')[12]
    console.log(rsi.textContent)
    ws.send(rsi.textContent)
}, 3000);


  ```
