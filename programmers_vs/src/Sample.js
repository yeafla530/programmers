export default class Sample {

    $target = null

    constructor($target) {
        this.$target = $target

        const $h1 = document.createElement('h1')
        $h1.innerText = '샘플 프로젝트'
        const $h2 = document.createElement('h2')
        $h2.innerText = '안녕하세요 ggg'

        $target.appendChild($h1)
        $target.appendChild($h2)
    }
}