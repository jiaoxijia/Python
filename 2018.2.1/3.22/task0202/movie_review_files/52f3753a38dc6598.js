
Do(function(){
  var cookieCfg={key:"ap",cookie:"1"},$doubanTip=$("#doubanapp-tip"),data={};function hideDoubanTip(){if(!$doubanTip.length){return}$doubanTip.hide();data[cookieCfg.key]=cookieCfg.cookie;set_cookie(data)}$doubanTip.delegate("a","click",hideDoubanTip);if(!get_cookie(cookieCfg.key)){$doubanTip.show()}var popup;var nav=$("#db-global-nav");var more=nav.find(".bn-more");function handleShowMoreActive(c){var a=$(c.currentTarget);var b=a.parent();hideDoubanTip();if(popup){popup.parent().removeClass("more-active");if($.contains(b[0],popup[0])){popup=null;return}}b.addClass("more-active");popup=b.find(".more-items");popup.trigger("moreitem:show")}nav.delegate(".bn-more, .top-nav-reminder .lnk-remind","click",function(a){a.preventDefault();handleShowMoreActive(a);return}).delegate(".lnk-doubanapp","mouseenter",function(b){var a=$(this);if(!a.parent().hasClass("more-active")){handleShowMoreActive(b)}}).delegate(".top-nav-doubanapp","mouseleave",function(){var b=$(this);var a=b.find(".lnk-doubanapp");if(popup){b.removeClass("more-active");if($.contains(b[0],popup[0])){popup=null}}});$(document).click(function(a){if($(a.target).closest(".more-items").length||$(a.target).closest(".more-active").length){return}if(popup){popup.parent().removeClass("more-active");popup=null}});
});

    Do(function() {
      $.getScripts=function(){var t=Array.prototype.slice.call(arguments);t.length&&!function i(c){if(c)return"function"==typeof c?void c():void $.ajax({url:c,dataType:"script",cache:!0,complete:function(){i(t.shift())}})}(t.shift())};

      $.getScripts(
        'https://img3.doubanio.com/f/shire/45dbd19d76e2601d4b8ac605bf7f1fefc4f34d10/js/lib/jquery.tmpl.min.js',
        'https://img3.doubanio.com/f/epstein/e1b3eda57ecf09b716e489e854ac81da234ac10e/js/movie/search_sugg.js',
        function() {
         $("#db-nav-movie").find("input[name=search_text]").iSuggest({
             api: '/j/subject_suggest',
             tmplId: 'suggResult',
             item_act: function(item){
                 window.location = item.data("link");
             }
         });
      });
    });
  
Do(function(){
    var nav = $('#db-nav-movie');
    var inp=$("#inp-query"),label=inp.closest(".nav-search").find("label");"placeholder"in inp[0]?(label.hide(),inp.attr("placeholder",label.text())):(""!==inp.val()&&label.hide(),inp.parent().click(function(){inp.focus(),label.hide()}).end().focusin(function(){label.hide()}).focusout(function(){""===$.trim(this.value)?label.show():label.hide()}).keydown(function(){label.hide()})),inp.parents("form").submit(function(){if(!$.trim(inp.val()).length)return!1}),nav.find(".lnk-more, .lnk-account").click(function(n){n.preventDefault();var i,e=$(this),t=e.hasClass("lnk-more")?$("#db-productions"):$("#db-usr-setting");t.data("init")||(i=e.offset(),t.css({"margin-left":i.left-$(window).width()/2-t.width()+e.width()+parseInt(e.css("padding-right"),10)+"px",left:"50%",top:i.top+e.height()+"px"}),t.data("init",1),t.hide(),$("body").click(function(n){var i=$(n.target);i.hasClass("lnk-more")||i.hasClass("lnk-account")||i.closest("#db-usr-setting").length||i.closest("#db-productions").length||t.hide()})),"none"===t.css("display")?($(".dropdown").hide(),t.show()):$(".dropdown").hide()});

});

        Do(function(){
            // 防止页面没加载完的时候，点击 tab 的切换
            $('#cinemas-section .tab-hd a').bind('click', function(e){
                e.preventDefault();
            })
        });

        Do.ready(
        'https://img3.doubanio.com/f/shire/45dbd19d76e2601d4b8ac605bf7f1fefc4f34d10/js/lib/jquery.tmpl.min.js',
        'https://img3.doubanio.com/f/epstein/4db11850d18304c5ffa21d9d8cde8aa433fa128c/js/movie/subject_detail_tip.js',
        'https://img3.doubanio.com/f/epstein/2796f81f0ac4cc7bcd75368ab12a341ed81449b4/js/movie/hot_cities.js',
        'https://img3.doubanio.com/f/shire/3d185ca912c999ee7f464749201139ebf8eb6972/js/ui/dialog.js',
        'https://img3.doubanio.com/f/epstein/e3e4c0d1b9ccf095c0e6704bf08f3cef62e8b254/js/movie/pop_ticket.js',
        function(){
            var city = '108296',
                cityName = '上海';

            $('.poster img').subjectTip('.list-item');

            var hot = new HotCities({'trigger': '.change-loc'});
            hot.init();

            function _popTicket(event) {
                event.preventDefault();

                var $this = $(this),
                    $list = $this.parents('.list-item'),
                    $chart = $this.parents('.chart-item'),
                    $data = $list.length? $list: $chart,
                    subject = $data.data('subject'),
                    _title = '《' + $data.data('title')  + '》',
                    title = $this.hasClass('ticket-btn')? _title + '选座购票': _title + '查影讯',
                    source = $data.data('category') + '_' + $this.data('source'),
                    data = {
                        title: title,
                        subject: subject,
                        city: city,
                        cityName: cityName,
                        source: source
                    };

                if ($data.data('category') === 'upcoming' && !$this.hasClass('ticket-btn')) {
                    data.title = _title + '影片详情';
                }

                popTicket(data);
            }

            $('body')
                .delegate('#nowplaying .poster a, #nowplaying .title a,                             #upcoming .poster a, #upcoming .title a,                             .chart-item h3 a,                             .list-item .sbtn a,                             .chart-item .mod-bd .sbtn',
                        'click', _popTicket)
                .delegate('#change-location', 'click', function(e) {
                    var pop = top.frames['ticket-popup'],
                        $citiesList = pop.$('#cities-list');

                    $citiesList.toggle();
                })
                .delegate('.ticket-popup .dui-dialog-close', 'click', function(e) {
                    var newCity = $('#change-location').data('changeto'),
                        oldCity = $('#location').data('uid');

                    if (newCity && newCity !== oldCity) {
                        window.location.href = '/cinema/nowplaying/' + newCity;
                    }
                })
                .delegate('.more', 'click', function(e) {
                    $.get('/blank?from=mov_ticket_index_page_playing_more');
                    $('#nowplaying .hidden').removeClass('hidden');
                    $(this).remove();
                });
        });
    
    Do.ready(
    'https://img3.doubanio.com/f/shire/45dbd19d76e2601d4b8ac605bf7f1fefc4f34d10/js/lib/jquery.tmpl.min.js',
    'https://img3.doubanio.com/f/shire/90edf76423e640e2e2e3539a87d8fa1753ca41d8/js/core/cookie.js',
    'https://img3.doubanio.com/f/epstein/e3e4c0d1b9ccf095c0e6704bf08f3cef62e8b254/js/movie/pop_ticket.js',
    function(){
        var city = '108296',
            cityName = '上海';

        function _genCinemas(e,i){var t=$("<ul>"),a=$("#cinema-item-tpl"),n=!1;return"search"===i&&(n=!0),e.length?$.each(e,function(e,i){var c={id:i.site_id,name:i.name,address:i.address,can:i.exist_sellable_schedule,ticket:i.can_sell,search:n,url:i.url,telephone:i.telephone};t.append(a.tmpl(c))}):n||"districts"===i?t.append('<li class="search-tip">未能搜索到相关影院</li>'):t.append('<li class="search-tip">抱歉，豆瓣的影讯尚未覆盖到你所在城市</li>'),t.html()}_interval=null;var limit=10,ck=get_cookie("ck"),data={city_id:city,limit:limit};$.get("/j/cinema/cinemas/",data,function(e){var i=_genCinemas(e,"default");$("#default-section").find(".cinema-items").empty().append(i).end().addClass("on"),$("#cinemas-section .tip").hide()}),$.get("/j/cinema/cinemas/",{city_id:city},function(e){var i=_genCinemas(e,"districts");$("#districts-section .cinema-items").empty().append(i)}),$("#cinemas-section").delegate(".tab-hd a","click",function(e){e.preventDefault();var i=$(this),t=i.attr("href");switch(i.parents("ul").find(".on").removeClass("on").end().end().parents("li").addClass("on"),$("#cinemas-section .bd").find(".on").removeClass("on"),$(t).addClass("on"),t){case"#districts-section":$("#all").trigger("click");break;case"#search-section":$("#search-section").find(".search-input").text("").end().find(".cinema-items").empty()}}).delegate(".cinema-item","mouseover",function(e){$("#cinemas-section .cinema-item").removeClass("hover"),$(this).addClass("hover")}).delegate(".district-item","click",function(e){var i=$(this).attr("id"),t={city_id:city};$("#districts li").removeClass("active"),$(this).parents("li").addClass("active"),"all"!==i&&(t.district_id=i);var a=$("#districts-section .cinema-items");a.empty().append('<li class="search-tip">正在加载...</li>'),$.get("/j/cinema/cinemas/",t,function(e){var i=_genCinemas(e,"districts");a.empty().append(i)}),$.get("/blank?from=new-district-item")}).delegate("#search .search-input","keyup",function(e){var i=$(this),t=$.trim(i.val());_interval&&(clearTimeout(_interval),_interval=null),t&&(_interval=setTimeout(function(){$.post("/j/cinema/search",{city_id:city,q:t,ck:ck,limit:6,from:"new-cinema-section"},function(e){var i=$("#search-section .cinema-items"),t=_genCinemas(e.cinemas,"search");i.empty().append(t)})},200))}).delegate("#search .search-btn","click",function(e){var i=$.trim($("#search .search-input").val());i&&$.post("/j/cinema/search",{city_id:city,q:i,ck:ck,limit:6,from:"new-cinema-section"},function(e){var i=$("#search-section .cinema-items"),t=_genCinemas(e.cinemas,"search");i.empty().append(t)})}).delegate(".cinema-item","click",function(e){var i=$(this),t=i.attr("id"),a=$("#cinemaz-subjects-tpl"),n=i.data(),c=$("#cinemas-section .tab-hd .on a").attr("href").substr(1);n.id=t,$.get("/blank?from=new-cinema-item&section="+c),$.get("/j/cinema/"+t+"/playing_movies",function(e){n.subjects=e,$("#cinemaz-subjects").empty().append(a.tmpl(n)).show()})}).delegate("#cinemaz-subjects .btn-shut","click",function(e){e.preventDefault(),$("#cinemaz-subjects").empty().hide()}).delegate(".cinemaz-bd li a","click",function(e){e.preventDefault();var i=$(this),t=i.parents("#cinemaz-subjects").find("h3").data("cansell"),a="《"+i.text()+"》",n=t===!0?a+"选座购票":a+"查影讯",c=i.attr("id"),s=i.parents("#cinemaz-subjects").find("h3").data("cinema"),m={title:n,subject:c,city:city,cityName:cityName,cinema:s,source:"new_cinema_section"};popTicket(m),$.get("/blank?from=new-cinema-subject")});
    });

    $(function(){function i(){var i=$(".view_1 > li:first-child");i.find(".right_span").hide(),i.find(".text").show(),$(".view_1 li").on("mouseover",function(){var i=$(this);i.find(".right_span").hide(),i.siblings().find(".right_span").show(),i.find(".text").show(),i.siblings().find(".text").hide(),i.addClass("ba_co").siblings().removeClass("ba_co")})}function s(){var i=$(".tab_nav li"),s=$(".movie_ranking_time span");i.eq(0).addClass("hover"),i.on("click",function(){var i=$(this);s.text(i.data("date")),i.addClass("hover").siblings().removeClass("hover");var n=i.index();$(".tab_view > li").eq(n).show().siblings().hide()})}i(),s()});
