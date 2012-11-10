$(document).ready(function(){

    $('#pofile').change(function(){
        $('#btn_upload').show();
    });
    
    var $window = $(window);
    $('.po_action').affix({
        offset: {
            top: 50,
            bottom: 270
        }
    });
    
    $('#quick-search').keyup(function(){
        var filter = $(this).val();
        
        $('.msgid').each(function(){
            if($(this).text().search(new RegExp(filter,"i")) < 0){
                $(this).parent().hide();
            }else{
                $(this).parent().show();
            }
        });
    });
    
});
