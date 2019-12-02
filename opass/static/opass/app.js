$(function () {
    const moneyFmt = new Intl.NumberFormat('el-EL', {
        style: 'currency',
        currency: 'EUR',
        minimumFractionDigits: 2,
    });
    const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const frm = $("#frmOpass");
    const results = $("#results");
    results.hide();
    frm.submit((e) => {
            e.preventDefault();
            $.json(URL_CALCULATE, frm[0]).then(
                function (response) {
                    const head = $("#table thead tr");
                    head.html("");
                    const body = $("#table tbody tr");
                    body.html("");
                    MONTHS.forEach((month, index) => {
                        const th = $("<th>");
                        th.html(month);
                        head.append(th);
                        const cell = $("<td>");
                        cell.html(moneyFmt.format(response[index + 1]));
                        body.append(cell);
                    });
                    results.show()
                },
                function (xhr) {
                    if (xhr.status === 422) {
                        const error = JSON.parse(xhr.response);
                        Metro.toast.create(error.message, null, null, "alert");
                    } else {
                        Metro.toast.create(xhr.statusText, null, null, "alert");
                    }
                }
            );
            return false;
        }
    );
});