import axios from 'axios';

const client = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/'
});

const instance = axios.create();
instance.interceptors.request.use(function() {
    /*...*/
});

export default {
    async execute(method, resource, data) {
        return client({
            method,
            url: resource,
            data,
            headers: {}
        })
            .then(req => {
                return req.data;
            })
            .catch(error => {
                if (error.response) {
                    alert(error.response.data.errors.body);
                }
            });
    },
    getArticle(slug) {
        return this.execute('get', `/articles/${slug}`);
    },
    getArticles() {
        return this.execute('get', '/articles');
    },
    postSentenceSimilarity(sentence) {
        return this.execute('post', '/similar', sentence);
    },
    createArticle(article) {
        return this.execute('post', '/articles', article);
    }
};
