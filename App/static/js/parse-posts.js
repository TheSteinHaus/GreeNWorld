$('#search').hideseek({hidden_mode: true});

document.querySelector('#search').oninput = function () {
    if (!$(this).val()) {
        $('.list-main').find('li').hide("slow");
    }
}
