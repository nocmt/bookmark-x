/* 封装ajax函数
例子：
ajax({
    url: "./TestXHR.aspx",              //请求地址
    type: "POST",                       //请求方式
    data: { name: "super", age: 20 },        //请求参数
    dataType: "json",
    success: function (response, xml) {
        // 此处放成功后执行的代码
    },
    fail: function (status) {
        // 此处放失败后执行的代码
    }
});
 */
function ajax( options ) {
  options = options || {};
  options.type = ( options.type || "GET" ).toUpperCase();
  options.dataType = options.dataType || "json";
  let params = formatParams( options.data );

  //创建 - 非IE6 - 第一步
  if( window.XMLHttpRequest ) {
      var xhr = new XMLHttpRequest();
  } else { //IE6及其以下版本浏览器
      var xhr = new ActiveXObject( "Microsoft.XMLHTTP" );
  }

  //接收 - 第三步
  xhr.onreadystatechange = function () {
      if( xhr.readyState == 4 ) {
          let status = xhr.status;
          if( status >= 200 && status < 300 ) {
              options.success && options.success( xhr.responseText, xhr.responseXML );
          } else {
              options.fail && options.fail( status );
          }
      }
  }

  //连接 和 发送 - 第二步
  if( options.type == "GET" ) {
      xhr.open( "GET", options.url + "?" + params, true );
      xhr.send( null );
  } else if ( options.type == "POST" ) {
      xhr.open( "POST", options.url, true );
      //设置表单提交时的内容类型
      xhr.setRequestHeader( "Content-Type", "application/x-www-form-urlencoded" );
      xhr.send( params );
  }
}

/* 封装 jsonp 函数
*/
function jsonp( options ) {
  options = options || {};
  if( !options.url || !options.callback ) {
      throw new Error( "参数不合法" );
  }

  //创建 script 标签并加入到页面中
  let callbackName = ( "jsonp_" + Math.random() ).replace( ".", "" );
  let oHead = document.getElementsByTagName("head")[0];
  options.data[options.callback] = callbackName;
  let params = formatParams( options.data );
  let oS = document.createElement( "script" );
  oHead.appendChild( oS );

  //创建jsonp回调函数
  window[callbackName] = function( res ) {
      oHead.removeChild( oS );
      clearTimeout( oS.timer );
      window[callbackName] = null;
      options.success && options.success( res );
  };

  //发送请求
  oS.src = options.url + "?" + params;

  //超时处理
  if( options.time ) {
      oS.timer = setTimeout(function() {
          window[callbackName] = null;
          oHead.removeChild( oS );
          options.fail && options.fail({ message: "超时" });
      }, options.time );
  }
}

//格式化参数
function formatParams( data ) {
  let arr = [];
  for( let name in data ) {
      arr.push( encodeURIComponent(name) + "=" + encodeURIComponent(data[name]) );
  }
  arr.push( ("t=" + Math.random()).replace( ".", "" ) );
  return arr.join( "&" );
}
