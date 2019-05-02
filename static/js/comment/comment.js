// 初始化子评论
function init_comment(items){
    lis = ''
    for(var i =0; i < items.length; i++){
        data = items[i]
        item = '<div class="commentator commentator-child" id="comment-child-'+data.id+'" onmouseenter="EnterFunction(this)" onmouseleave="LeaveFunction(this)">'+
            '<div class="commentator-img">'+
                '<a href="/account/author/'+data.from+'">'+
                    '<img src="/media/avator/'+data.from+'.jpg" class="layui-nav-img" alt="">'+
                '</a>'+
            '</div>'+
            '<div class="commentator-info">'+
                '<a href="/account/author/'+data.from+'" class="commentator-name">'+data.from+'</a>'+
                '<span style="margin:0 10px">回复</span>'+
                '<a href="/account/author/'+data.to+'">'+data.to+'</a>'+
                '<span style="margin-left:20px">'+ data.created+'</span>'+
            '</div>'+
            '<div class="comment-wrap">'+
                '<pre>'+data.body+'</pre>'+
            '</div>'+
            '<div class="meta">'
        if('{{request.user.username}}'==data.from){
             item += '<a href="javascript:void(0)" onclick="comment_reply_delete('+data.id+', this)" class="comment-tool comment-delete"><span><i class="layui-icon layui-icon-delete"></i> <span>删 除</span></span></a>'
        }else{
            item += '<a href="javascript:void(0)" onclick="comment_report()" class="comment-tool comment-report"><span><i class="layui-icon layui-icon-release"></i> <span>举 报</span></span></a>'
            item += '<a href="javascript:void(0)" comment_id="'+data.id+'" class="comment_reply comment-tool" onclick="comment_reply(this)"><span><i class="layui-icon layui-icon-reply-fill"></i> <span class="tool-text tool-reply">回 复</span></span></a>'
        }
            item += '</div>'+
                '<div class="reply_input" comment_id="'+data.id+'"></div>'+
            '</div>'

        lis += item
    }
    return lis
}