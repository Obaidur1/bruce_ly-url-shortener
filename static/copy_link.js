document.addEventListener("DOMContentLoaded", function() {
    const copyButtons = document.querySelectorAll(".copy-btn");

    copyButtons.forEach(button => {
        button.addEventListener("click", function() {
            const linkToCopy =  this.getAttribute("short_url");
            copyToClipboard(linkToCopy);


            const tooltip = document.createElement('div');
            tooltip.classList.add('tooltip');
            tooltip.textContent = 'Copied!';
            const buttonRect = button.getBoundingClientRect();
            tooltip.style.left = buttonRect.left + 'px';
            tooltip.style.top = buttonRect.top - 30 + 'px';
            document.body.appendChild(tooltip);
            setTimeout(() => {
                document.body.removeChild(tooltip);
            }, 1000);

        });
    });
});

function copyToClipboard(text) {
    const baseAddress = window.location.protocol + "//" + window.location.host+"/";
    const url = baseAddress+text
    navigator.clipboard.writeText(url)
    document.dispatchEvent(new ClipboardEvent("copy", { url }));
    
}
