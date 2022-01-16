// Code goes here
$(document).ready(function() {

	// page is now ready, initialize the calendar...

  	var calendar = $('#calendar').fullCalendar({
    // put your options and callbacks here
    	header: {
      		left: 'prev,next today',
      		center: 'title',
      		//right: 'year,month,basicWeek,basicDay'
      		right: 'year,month'
		},
	    timezone: 'local',
	    height: "auto",
	    selectable: true,
	    dragabble: true,
	    defaultView: 'month',
	    yearColumns: 3,
	    eventLimit: true,

    	durationEditable: true,
    	bootstrap: false,

    	events: function(start, end, timezone, callback) {
            $.ajax({
            	url: 'user/get_events',
            	dataType: 'json',
            	data: {
            	// our hypothetical feed requires UNIX timestamps
            	start: start.unix(),
            	end: end.unix()
            	},
            	success: function(msg) {
                	var events = msg.events;
                	callback(events);
            	}
            });
        },
		eventRender: function(event, element) { 
            element.find('.fc-title').append(" - " + event.description); 
        },
    	select: function(start, end, allDay) {
			saveevents(start, end, allDay);
    	},
  	})
  
  	var start_date = '';
  	var end_date = '';
  	function saveevents(start, end, allDay){
  		$('#modal-calender').modal('show');
  		start_date = start.unix();
        end_date = end.unix();
  	}
  	
  	$("#e_form").validate(
	{
		ignore: null,
		ignore: 'input[type="hidden"]',
		submitHandler: function(form)
		{
			var e_type = $("#e_type").val();
			var desc = $("#desc").val();
			
			if(desc==''){
				alert("Please Enter ther Desc...");
				return false;
			}
			/*alert(e_type);
			return false;*/
			var req = new Request();
			req.url ="user/add_events";
			req.data =
			{
				"title":e_type,
				"desc":desc,
				"start":start_date,
				"end":end_date
			}

			RequestHandler(req,add_eventsform);
		}
	});

	function add_eventsform(data)
	{	
		data = JSON.parse(data);
		$("#div_success").css("display","none");
		$("#div_error").css("display","none");
		if(data.iserror == true)
		{
			$("#span_err").html(data.message);
			$("#div_error").css("display","block");		
		}
		else
		{		
			$("#div_success").css("display","block");		
		 	location.reload();
		}	
	}
});