### 监控脚本
* [pm2 for nodejs and python .sh perl ...](https://juejin.im/post/5bbc1a5e6fb9a05d3634f639)
* [pm2-gui](https://github.com/Tjatse/pm2-gui)


### web

#### [URI 获取操作URL的库](https://github.com/medialize/URI.js)
* [URI](https://medialize.github.io/URI.js/)
* [build URI JS](http://medialize.github.io/URI.js/build.html)
* [get url param](https://smoothprogramming.com/tutorials/get-set-query-string-values-from-url-using-uri-js/)


### wordpress

* http://domain/wp-admin/
* http://domain/wp-login.php

### JS

* sleep 
```

// https://zeit.co/blog/async-and-await
function sleep(time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}

// 用法
sleep(500).then(() => {
    // 这里写sleep之后需要去做的事情
})

async function showList() {

    await sleep(1500);
}

```
