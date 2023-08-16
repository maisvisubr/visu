let video_container = document.getElementById('video_container')

function createComponent(titulo, url, desc, segundos){
    let component = `
    
    `
    return component
}

$.ajax({
    method:'POST',
    url:'/getvideos',
    success:function(data){
        let obj = JSON.parse(data)

        obj.forEach(el => {
            let component = createComponent(el.titulo, el.url, el.desc, el.segundos)
            video_container.innerHTML += component
        });
    }
})