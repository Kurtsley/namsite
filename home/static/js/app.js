(function () {
    // Initialize flatpickr when the DOM is ready
    document.addEventListener("DOMContentLoaded", function () {
        flatpickr("#datepicker", {
            dateFormat: "m-d-Y",
            defaultDate: "01-01-2024",
            inline: true,
            position: "auto center",
            disableMobile: true,
            onChange: function (selectedDates, dateStr, instance) {
                if (dateStr) {
                    // Convert seledted date to proper format
                    const date = dateStr.split('-');
                    const month = date[0];
                    const day = date[1];
                    const mmdd = `${month}-${day}`;

                    fetch(`/check-date/${mmdd}/`)
                        .then(response => response.json())
                        .then(data => {
                            const title = document.getElementById("result-title");
                            const paragraph = document.getElementById("result-paragraph");
                            const explanationParagraph = document.getElementById("explanation-paragraph");
                            const resultPanel = document.getElementById("result-panel");

                            if (data) {
                                title.textContent = data.title;
                                paragraph.textContent = data.message;

                                explanationParagraph.innerHTML = '';

                                if (data.explanations) {
                                    const separator = document.createElement('hr');
                                    separator.classList.add('separator');

                                    explanationParagraph.insertBefore(separator, explanationParagraph.lastChild);

                                    const explanations = Array.isArray(data.explanations) ? data.explanations : data.explanations.split(',');
                                    explanations.forEach(explanation => {
                                        explanationParagraph.insertAdjacentHTML('beforeend', `<p>${explanation}</p>`);
                                    });
                                }
                            }
                            else {
                                explanationParagraph.textContent = "";
                            }
                            resultPanel.scrollIntoView({ behavior: "smooth", block: "center" });
                        });
                }
            }
        });
    });
})();
