~function(t,e){t.fn.subjectTip=function(i,n){t(this).hover(function(o){e._showtip=setTimeout(function(){t("#subject-tip").remove();var e=t(o.target),c=e.parents(i).data(),s=t("#db-tmpl-subject-tip").tmpl(c),p=e.offset();e.width();"screening"===n&&s.addClass("screening-tip"),s.css({left:p.left+e.width()+8,top:p.top}).appendTo(t("body")).show()},400)},function(){clearTimeout(e._showtip),t("#subject-tip").remove()}),t(document).unbind("click.removeTip").bind("click.removeTip",function(e){t(e.target).parents("#subject-tip").length||t("#subject-tip").remove()})}}(jQuery,window);