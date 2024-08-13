function search() {
    let query = document.getElementById('search').value.toLowerCase();
    let publications = document.querySelectorAll('.publication');
    publications.forEach(publication => {
        let text = publication.innerText.toLowerCase();
        if (text.includes(query)) {
            publication.style.display = '';
        } else {
            publication.style.display = 'none';
        }
    });
}

function sortPublications() {
    let sortOption = document.getElementById('sort').value;
    let publications = Array.from(document.querySelectorAll('.publication'));

    publications.sort((a, b) => {
        let aData = a.dataset;
        let bData = b.dataset;

        switch (sortOption) {
            case 'year-desc':
                return bData.year - aData.year;
            case 'year-asc':
                return aData.year - bData.year;
            case 'author-asc':
                return aData.author.localeCompare(bData.author);
            case 'author-desc':
                return bData.author.localeCompare(aData.author);
            case 'n-desc':
            default:
                return bData.n - aData.n;
        }
    });

    let publicationsList = document.querySelector('.publications-list');
    publicationsList.innerHTML = '';
    publications.forEach(pub => publicationsList.appendChild(pub));
}

