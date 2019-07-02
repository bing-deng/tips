### 常用方法


* 查看子字符串个数

```
var last_num = "a"
var s = "abcaa"
var reg = new RegExp(last_num, "g");
console.log(s.match(reg).length)
```

* js sleep 实现  [参考](https://www.sejuku.net/blog/24629)
```

// ビジーwaitを使う方法
function sleep(waitMsec) {
  var startMsec = new Date();
 
  // 指定ミリ秒間だけループさせる（CPUは常にビジー状態）
  while (new Date() - startMsec < waitMsec);
}
 
sleep(5000);
 
// 5秒後にメッセージを表示
console.log('5秒経過しました！');


```

  * sleep by promise
  ```
  
  window.onload = function () {
 
    // Promiseを使う方法
    function sleepByPromise(sec) {
 
        return new Promise(resolve => setTimeout(resolve, sec*1000));
 
    }
 
    // async修飾子を使って非同期関数を宣言します。
    async function wait(sec) {
 
        console.log('wait ' + sec.toString() + ' sec right now!');
 
        // await句を使って、Promiseの非同期処理が完了するまで待機します。
        await sleepByPromise(sec);
 
        console.log('wait ' + sec.toString() + ' sec done!');
 
    }
 
    console.log('anothor task 1 ');
    console.log('anothor task 2 ');
    wait(5);
    console.log('anothor task 3 ');
    console.log('anothor task 4 ');
 
}
  ```
