function deleteProject(i){
    event.preventDefault(true);
    let fields = document.forms["project-form-"+i].getElementsByTagName("input");
    let csrf_token_entry = fields[0].value;
    let data = JSON.stringify({
        entryNo : i,
    });
    $.ajax({
        url: 'update-project/',
        type: 'DELETE',
        dataType: 'json',
        data: data,
        beforeSend: function(request) {
            request.setRequestHeader('X-CSRFToken', csrf_token_entry);
        },
        success: function(result) {
            if (result.success){
                let deletedForm = $("#project-" + i);
                deletedForm.animate({
                    'padding': "0px",
                    'margin-left':'-10px',
                    'font-size': "0px"
                }, 400, function() {
                    deletedForm.remove();      
                });
            } else {
                document.getElementById("update-status").innerText = "Something wrong happened.";
                $('#response-modal').modal('show');
            }
        }
    });
}