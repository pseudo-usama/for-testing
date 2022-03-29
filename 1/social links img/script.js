var shotit = function () {
    html2canvas(document.querySelector('ul'), {
        onrendered: function (canvas) {
            document.body.appendChild(canvas)
            leCanvas = document.getElementsByTagName("canvas")[0]
            var img = leCanvas.toDataURL("image/png")
            document.write('<span style="font:14px normal Helvetica, Arial; font-weight: bold; color:#13a6f5; margin-left:16px">the resulted png:</span> <br /><img src="' + img + '"/>')
        },
        width: 390,
        height: 220
    })
}