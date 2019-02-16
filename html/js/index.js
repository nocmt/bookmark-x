// 搜索Enter键事件
function search(e) {
    if (e.keyCode == 13) {
        var val = document.getElementById("search-field").value;
        window.open("https://google.com/search?q=" + val);
    }
}


// 获取当前时间和格式
function getTime() {
    let date = new Date(),
        min = date.getMinutes(),
        sec = date.getSeconds(),
        hour = date.getHours();

    return "" +
        (hour < 10 ? ("0" + hour) : hour) + ":" +
        (min < 10 ? ("0" + min) : min) + ":" +
        (sec < 10 ? ("0" + sec) : sec);
}


// 选项卡切换
function switchTab(dataId) {
    // 请求缓存，避免重复请求
    // 待开发

    // 选项切换标识
    let ats = document.getElementsByTagName("li");
    for(let v of ats) {
        if((v.getAttribute('data-id') === dataId)){
            v.classList.add('menu-action');
        }else{
            v.classList.remove('menu-action');
        }
      }

    let html = "";
    let item = "";
    ajax({
        url: 'http://nocmt.com/test/bookmark.json', // 请求地址
        type: 'POST', // 请求类型，默认"GET"，还可以是"POST"
        data: {
            // 'sort': sort
        }, // 传输数据
        dataType: "json",
        success: function (response, xml) { // 请求成功的回调函数
            // console.log(JSON.parse(response));
            let result = JSON.parse(response);
            if (result.success) {
                // console.log(result.success);
                item = result.result.data;
                for (let i = 0; i < item.length; i++) {
                    // console.log(item[i].id);
                    html += `<a target="_blank" href="//${item[i].link}">
                    <img width="20" src="${item[i].imgurl}" alt="">
                    <span class="text">${item[i].title}</span>
                </a>`;
                    // console.log(html);
                }
                document.getElementById('main').innerHTML = html;
            }

        },
        fail: function (status) {
            console.log(status);
        } // 请求失败的回调函数
    });
}

window.onload = () => {
    document.getElementById("clock").innerHTML = getTime(); // 设置时钟
    setInterval(() => {
        document.getElementById("clock").innerHTML = getTime(); // 将时钟间隔设置为滴答时钟
    }, 100);
}