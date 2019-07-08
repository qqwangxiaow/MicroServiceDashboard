$.extend({
    myMethod: function (id,tagData,name,html,Aname,fileId,seb) {
    	$(id).append(html)
        $(Aname).parent().hide();
	    //获取当前广告
	    $(fileId).on("click","dl dd",function(){
	    	var id = $(this).attr("value");
	    	if(id!=undefined){
	    		$(Aname).append('<a href="javascript:;" class="label"><span lay-value="64">'+$(this).html()+'</span><input type="hidden" name="'+name+'" id="'+$(this).html()+'" value="'+id+'"/><i class="layui-icon close">x</i></a>')
	    		$(Aname).parent().show(300);
	    		for(var i=0;i<tagData.length;i++){
	    			if(tagData[i].id == id){
	    				tagData.splice(i,1);
	    			}
	    		}
	    	}
	    	$(fileId+" dl").hide();
	    	$(fileId+" input").val("");
		})

		function AD(name,id){
            this.name=name;
            this.id=id;
        }

	 	//删除当前广告
		$(Aname).on("click",".close",function(){
			$(this).parent().remove();
			var id = $(this).parent().children("input").val();
			var text = $(this).parent().children("input").attr("id");
			tagData.push(new AD(text,id))
			if($(Aname+" "+".label").length == 0){
			    $(seb).hide(300);
			}
		})

		//筛选
	    $(fileId+" input").on("input propertychange",function(){
	    	$(fileId+" dl dd").remove();
	    	$(fileId+" dl").hide();
    		if(tagData.length>0){
    			$(".fileId dl").show();
    			var sear = new RegExp($(this).val())
    			var temp=0;
	    		for(var i=0;i<tagData.length;i++){
	    			if(sear.test(tagData[i].name)){
	    				temp++
		    			$(fileId+" dl").append('<dd value="'+tagData[i].id+'">'+tagData[i].name+'</dd>')
	    			}
	    		}
	    		if(temp==0){
	    			$(fileId+" dl").append('<dd>No Data</dd>')
	    		}
    		}
	   	})

	   	//隐藏
	   	$(document).click(function(){
			$(fileId+ "dl").hide();
	    	$(fileId+" input").val("");
		});

	 	//显示没被选择的
		$(fileId+" input").click(function(event){
			$(fileId+" dl dd").remove();
	    	if(tagData.length==0){
				$(this).val("No Data")
	    	}else{
		    	$(fileId+" dl").show()
	    	}
	    	for(var i=0;i<tagData.length;i++){
	    		$(fileId+" dl").append('<dd value="'+tagData[i].id+'">'+tagData[i].name+'</dd>')
    		}
			event.stopPropagation();
		});

    }
});


