 function getExtension(filename) {
    return filename.split('.').pop().toLowerCase();
}

 function setImageVisible(id, visible) {
    	var img = document.getElementById(id);
    	img.style.visibility = (visible ? 'visible' : 'hidden');
	}

 function readURL(input,num) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
        	reader.onload = function (e) {
            	$('#preview').attr('src', e.target.result);
        	}
            reader.readAsDataURL(input.files[0]);
        }
    }


$(function() {
 $("#file").change(function (){
 	$("#upload").attr("type","submit");
 	var pathFile = $("#file").val();
 	
 	switch(getExtension(pathFile)) {
        case 'jpg':
        	if ( $('#divPreview').children().length > 0 ) {
    			$("#preview").remove();
    			$('#divPreview').append('<center><img id="preview" src="" alt="" height="390" width="300"></center>');
				readURL(this);

			}else{
				$('#divPreview').append('<center><img id="preview" src="" alt="" height="390" width="300"></center>');
				readURL(this);

			};	
            break;
        case 'pdf':
        	if ( $('#divPreview').children().length > 0 ) {
    			$("#preview").remove();
    			$('#divPreview').append('<center><iframe id="preview" frameborder="0" scrolling="no" width="300" height="390"></iframe></center>');
				readURL(this);

			}else{
				$('#divPreview').append('<center><iframe id="preview" frameborder="0" scrolling="no" width="300" height="390"></iframe></center>');
				readURL(this);

			};
            break;

    }
 });
});


    
    