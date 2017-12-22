/*获取控制对象*/	
var vids=document.getElementById("vids");
var sskd=$(".controls").width();/*替换原来的764*/
/*一开始默认的视频路径（每个页面都会有一个默认的视频吧）*/
// var csdz=" ../";
/*这一步判断他是什么浏览器，调用不同的格式的视频（这里以mp4为例子）*/
// var xzdz="https://201712mp4.89soso.com/20171208/16/1/xml/91_d595a48c14f44bbd9b69bdb1498ffe21.mp4";
var xzdz="{{tages.urls}}";
vids.src=xzdz;
/*点击右边的话替换左边视频的地址链接以及替换播放器的名字*/
$(".one_tb").click(function(){
	//$(this).addClass("on").siblings(".one_tb").removeClass("on");
	//var hName=$(this).find("h3").html();
	//var vid_src=$(this).attr("vid_src");
	//$(".title_top").html(hName);
	//vids.src=vid_src+xzdz;
	vids.src=xzdz;
	vids.play();
	})
/*点击暂停图标的时候*/		
$("#pass").click(function(){
	$(this).css({display:"none"});
	$("#ztbf").attr("class","iconfont icon-zanting")
	vids.play();
	});
/*点击控制按钮里面的暂停图标的时候*/	
$("#ztbf").click(function(){	
	if(vids.paused){
		vids.play()
		$("#ztbf").attr("class","iconfont icon-zanting")
		}else{
			vids.pause()
			$("#ztbf").attr("class","iconfont icon-zanting2")
			}
})
/*不论任何途径只要是暂停或者播放*/
vids.onplay=function(){
	$("#pass").css({display:"none"});
	$("#ztbf").attr("class","iconfont icon-zanting");
	}
vids.onpause=function(){
	$("#pass").css({display:"block"});
	$("#ztbf").attr("class","iconfont icon-zanting2");
	$("#pBar").on('mouseup',function(){
			$(this).off('mousemove')
			})
	}
/*时间转换器*/
function numFormat(time){
    time = parseInt(time);
    var h = addZero(Math.floor(time/3600));
    var  m = addZero(Math.floor((time%3600)/60));
    var s = addZero(Math.floor(time%60));
    return h+":"+m+":"+s;
}
function addZero(num){
    if(num<10){
        return "0"+num;
    }else{
        return ''+num;
    }
}
/*当前时间/总的时间(canplay方法开始)*/
vids.oncanplay=function(){
var aTime=numFormat(vids.duration);
$("#aTime").html(aTime);
/*第一步,进度条跟着时间动(鼠标点下的时候)*/
vids.ontimeupdate=function(){
	sskd=$(".controls").width()
	var hc=(vids.buffered.end(0)/vids.duration)*sskd;
	$("#buff").css({width:hc+'px'})
	var nTime=numFormat(vids.currentTime);
	$("#nTime").html(nTime);
	/*当前的时间比上总的时间乘以总的长度*/
	var nLengh=(vids.currentTime/vids.duration)*(sskd-20);
	$("#pBar_move").css({width:nLengh+'px'});
	}
/*第二步,点击时的进度条*/
$("#pBar").mousedown(function(e){
	var cLk=e.clientX;/*点击距离(点击在进度条区域)*/
	var pJl=$("#pBar").offset().left;/*获取进度条距离左边的距离*/	
	var mLengh=cLk-pJl;/*移动的距离*/
	if(mLengh>=(sskd-20)){
		mLengh=(sskd-20)
		}
	$("#pBar_move").css({width:mLengh+'px'});/*改变进度条的距离*/
	var cTime1=mLengh/(sskd-20)*vids.duration;
	vids.currentTime=cTime1;
	var cTime2=numFormat(cTime1);
	$("#nTime").html(cTime2);/*改变html的显示时间*/
	vids.play();
/*---------------------------------鼠标拖拽的距离---------------------------------------*/
	$(document).on('mousemove',function(e){
		vids.pause();
		var newLeft=e.clientX-pJl;/*拖拽的距离*/
		if(newLeft<=0){
            newLeft=0;
        }
		if(newLeft>=(sskd-20)){
			newLeft=(sskd-20)
			}
		var cTime3=newLeft/(sskd-20)*vids.duration;
		var cTime4=numFormat(cTime3);
		$("#pBar_move").css({width:newLeft+'px'});
		vids.currentTime=cTime3;
		$("#nTime").html(cTime4);
		})/*拖拽结束*/
/*----------------------------------鼠标松开----------------------------------------*/
		$("body").on('mouseup',function(){
			$(document).off('mousemove');
			vids.play();
			})/*松开结束*/
	})/*mousedown方法结束*/
}/*(canplay方法结束)*/
/*----------------------------------快进快退(点击html的时候)----------------------------------*/	
function ktui(){
	vids.currentTime-=10;
}
function kjin(){
	vids.currentTime+=10;
}
/*----------------------------------快进快退(点击键盘的时候)----------------------------------*/
$(document).keydown(function (event) {
	if (event.keyCode===37){
		vids.currentTime-=10;
	}
	if (event.keyCode===39){
		vids.currentTime+=10;
	}
	/*----暂停播放(点击键盘空格的时候)----*/
	if (event.keyCode===32){
		if(vids.paused){
		vids.play()
		$("#ztbf").attr("class","iconfont icon-zanting")
		}else{
			vids.pause()
			$("#ztbf").attr("class","iconfont icon-zanting2")
			}
	}
	/*-----------退出全屏-----------*/
	if (event.keyCode===27){
		$(".video_ls").removeClass("on");
		$(".controls").css({width:"764px"})
	}
})
/*鼠标双击事件(双击播放器然后全屏)*/
$(".video_ls").dblclick(function(){
	$(".video_ls").addClass("on");
	var oBox=$("body").width()-66;
	$(".controls").css({width:oBox+'px'})
});
/*全屏播放按钮*/
$("#qp").click(function(){
	if($(".video_ls").hasClass("on")){
		$(".video_ls").removeClass("on");
		$(".controls").css({width:"764px"})
		}else{
			$(".video_ls").addClass("on");
			var oBox=$("body").width()-66;
			$(".controls").css({width:oBox+'px'})
			}
})	
/*收藏*/
$("#like").click(function(){
	if($(this).hasClass("on")){
		$(this).removeClass("on")
		}else{
			$(this).addClass("on")
			}
	})
/*点赞*/
$("#zan").click(function(){
	if($(this).hasClass("on")){
		$(this).removeClass("on")
		}else{
			$(this).addClass("on")
			}
	})
/*音量加减*/
vBtn.onmousedown = function(ev){
    var ev=ev||window.event;
    var xs=ev.clientX - this.offsetLeft;
    document.onmousemove = function(ev){
        var newLefts=ev.clientX-xs;
        if(newLefts<=0){
            newLefts=0;
        }else if(newLefts>=vBar.offsetWidth-vBtn.offsetWidth){
            newLefts=vBar.offsetWidth-vBtn.offsetWidth;
        }
        vBtn.style.left=newLefts+"px";
        vBar_in.style.width =(newLefts+8)+"px";
        var prop=newLefts/(vBar.offsetWidth-vBtn.offsetWidth);
        vids.volume =prop;
        //静音改变音量图标
        // if(!vids.volume){
        //     icon.style.backgroundImage="url(images/iconb.png)"
        // }else{
        //     icon.style.backgroundImage="url(images/icona.png)"
        // }
    }
	document.onmouseup = function(){
	document.onmousemove = null;
	document.onmouseup = null;
    }
}	
