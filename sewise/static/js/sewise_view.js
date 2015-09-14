/* Javascript for sewiseXBlock. */
function sewiseXBlockInitView(runtime, element) {
    /* Weird behaviour :
     * In the LMS, element is the DOM container.
     * In the CMS, element is the jQuery object associated*
     * So here I make sure element is the jQuery object */
     //get params from studio
     console.log("mytest");
     data = get_params(runtime, element);
     console.log("mytest");
}
function get_params(runtime, element){
    var sessionid=$("#sessionid").attr("data");
    console.log(sessionid);
	$.ajax({
            type: "POST",
            url: runtime.handlerUrl(element, 'get_params'),
            data: JSON.stringify({sessionid: sessionid}),
            success: function(result) {
                console.log(result);
                video_id = result.data.data;
                //return data
                //sewise_play(result.data);
            }
        });

}
