function updateInfo(){
    event.preventDefault(true);
    let fields = document.forms["info-form"].getElementsByTagName("input");
    let textarea = document.forms["info-form"].getElementsByTagName("textarea")
    let csrf_token_entry = fields[0].value;
    let data = JSON.stringify({
        name : fields[1].value,
        description : textarea[0].value,
        email : fields[2].value,
        linkedin : fields[3].value,
        git : fields[4].value,
        phone_number : fields[5].value,
        title : fields[6].value,
    });
    $.ajax({
        url: 'update-info/',
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