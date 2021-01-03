const posting = new Vue({
    el: '#posting',
    delimiters: ['${', '}'],
    data: {
        post: {},
        loading: true,
        id: getParameters('uid'),
        // message: null,
    },
    mounted: function () {
        this.getPost(this.id);
    },
    methods: {
        getPost: function (pk) {
            axios.get('/post/api/' + pk + '/')
                .then((response) => {
                    this.post = response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        },
        postPost: function () {
            axios.post('/post/api/', payload, headers = { "X-CSRFToken": csrftoken })
                .then((response) => {
                  this.post = response.data;
                  history.back();
                })
                .catch((err) => {
                  console.log(err);
                })
        },
        deletePost: function (pk) {
            axios.delete('/post/api/' + pk + '/')
                .then((response) => {
                    this.post = response.data;
                    history.back();
                })
                .catch((err) => {
                    console.log(err);
                })
        }
    },
})
