$('#calculateButton').on("click",
    e => {
        let mask_count_init = $('#mask_count_init').val();
        let mask_count_target = $('#mask_count_target').val();
        $.get('/knitting/calculate?target='
            + mask_count_target
            + "&init="
            + mask_count_init,
                result => {$('#resultContainer').html(result)});
    });
