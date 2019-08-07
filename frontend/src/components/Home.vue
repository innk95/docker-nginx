<template>
    <div>
        <auth></auth>
    </div>
</template>

<script>
    import Auth from '@/components/Auth'

    export default {
        name: "Home.vue",
        components: {
            'auth': Auth,
        },
        created () {
            this.getProfile()
        },
        data () {
            return {
            }
        },
        methods: {
            getProfile () {
                axios.get('/api/profile').then(response => {
                    if(response.data) {
                        this.$router.push({name: 'profile', params: {profile: response.data}})
                    }
                }).catch(response => {
                    alert('Технические ошибки')
                })
            }
        }
    }
</script>

<style>
    .my-margin {
        margin-top: 30px
    }
</style>