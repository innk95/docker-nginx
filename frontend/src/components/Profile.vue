<template>
    <div>
        <div class="row">
            <div class="col-md-4"></div>
            <div class="col-md-4 border">
                <div class="row">
                    <div class="col-md-12 my-margin">Данные пользователя</div>
                    <div class="col-md-12 my-margin"><input type="text" v-model="profile.username" class="form-control" placeholder="Логин"></div>
                    <div class="col-md-12 my-margin"><input type="text" v-model="profile.first_name" class="form-control" placeholder="Имя"></div>
                    <div class="col-md-12 my-margin"><input type="text" v-model="profile.last_name" class="form-control" placeholder="Фамилия"></div>
                    <div class="col-md-12 my-margin"><input type="email" v-model="profile.email" class="form-control" placeholder="email"></div>
                    <div class="col-md-12 my-margin">
                        <div class="row">
                            <div class="col-md-6 text-center">
                                <button class="btn btn-danger" @click="deleting">Удалить</button>
                            </div>
                            <div class="col-md-6 text-center">
                                <button class="btn btn-success" @click="change">Сохранить</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4 text-center my-margin">
                <button class="btn btn-warning" @click="logout">Выйти</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Profile",
        props: {
            profile: {
                type: Object,
                default: function () { return {} }
            }
        },
        data () {
            return {}
        },
        methods: {
            logout () {
                axios.post('/api/logout').then(response => {
                    this.$router.push({name: 'home'})
                }).catch(response => {
                    console.log('Технические ошибки')
                })
            },
            deleting () {
                axios.delete('/api/registration').then(response => {
                    this.$router.push({name: 'home'})
                }).catch(response => {
                    alert('Технические проблемы')
                })
            },
            change () {
                if (this.validate(this.profile.username, this.profile.email)) {
                    axios.post('/api/profile', {profile: this.profile}).then(response => {
                        alert('Пользватель изменен')
                    }).catch(response => {
                        alert('Логин уже занят')
                    })
                }
            },
            validate (login, email) {
                if (login.length < 4) {
                    alert('Логин должен быть больше 3-ех символов')
                    return false
                }
                let reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/
                if(reg.test(email) == false && email) {
                   alert('Введите корректный e-mail')
                   return false
                }
                return true
            }
        },
        mounted () {
            if (Object.entries(this.profile).length === 0) {
                this.$router.push({name: 'home'})
            }
        },
    }
</script>

<style scoped>

    .border {
        border: solid 1px;
        padding: 12px
    }

    .my-margin {
        margin-top: 10px
    }

    #danger-btns {
        margin-top: 50px
    }

</style>