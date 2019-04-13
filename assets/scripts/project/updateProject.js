function updateProject(i){
    event.preventDefault(true);
    let fields = document.forms["project-form-" + i].getElementsByTagName("input");
    let textarea = document.forms["project-form-" + i].getElementsByTagName("textarea")
    let csrf_token_entry = fields[0].value;
    let data = JSON.stringify({
        entryNo : i,
        name : fields[1].value,
        description : textarea[0].value,
        url : fields[2].value,
    });
    $.ajax({
        url: 'update-project/',
        type: 'PUT',
        dataType: 'json',
        data: data,
        beforeSend: function(request) {
            request.setRequestHeader('X-CSRFToken', csrf_token_entry);
        },
        success: function(result) {
            if (result.success){
                document.getElementById("update-status").innerText = result.message;
            } else {
                let errors = "";
                for (var key in result.message) {
                    result.message[key].forEach((er) => {
                        errors += er + "\n";
                    });
                }
                document.getElementById("update-status").innerText = errors;
            }
            $('#response-modal').modal('show');
        }
    });
}