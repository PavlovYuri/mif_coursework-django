var old_data = document.getElementById('old-data')
var new_data = document.getElementById('new-data')
var input_user_data = document.querySelectorAll(".input-user-data")
var change_user_data_btn = document.getElementById('change-user-data-btn')
var save_changes_user_data_btn = document.getElementById('save-changes-user-data-btn')

old_data.style.visibility = "hidden";
new_data.style.visibility = "hidden";

for (let i=0; i < input_user_data.length; i++) {
    input_user_data[i].style.visibility = "hidden";
};

save_changes_user_data_btn.style.visibility = "hidden";

change_user_data_btn.addEventListener("click", function(evt) {
    evt.preventDefault();
    old_data.style.visibility = "visible";
    new_data.style.visibility = "visible";

    for (let i=0; i < input_user_data.length; i++) {
        input_user_data[i].style.visibility = "visible";
    };

    save_changes_user_data_btn.style.visibility = "visible";
});

