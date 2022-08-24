const CSS_SELECTOR = "div[id^='chp_ads_block_modal_new']"


removePopUp()


function removePopUp() {
    document.querySelector(CSS_SELECTOR)
        .remove()
}
