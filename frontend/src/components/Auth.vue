<template>
    <div>
        <div class="row">
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <div class="row">
                    <div class="col-md-2"></div>
                    <div class="col-md-8 text-center border">
                        <div class="row">
                            <div class="col-md-12">Авторизация</div>
                            <div class="col-md-12 my-input">
                                <input class='form-control' type="text" v-model="login" placeholder="login">
                            </div>
                            <div class="col-md-12 my-input">
                                <input class='form-control' type="password" v-model="password" placeholder="password">
                            </div>
                            <div class="col-md-12 my-input">
                                <button class="btn btn-success" @click="authorization">Отправить</button>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2"></div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="row">
                    <div class="col-md-2"></div>
                    <div class="col-md-8 text-center border">
                        <div class="row">
                            <div class="col-md-12">Регистрация</div>
                            <div class="col-md-12 my-input">
                                <input class='form-control' type="text" v-model="login_reg" placeholder="login">
                            </div>
                            <div class="col-md-12 my-input">
                                <input class='form-control' type="password" v-model="password_reg" placeholder="password">
                            </div>
                            <div class="col-md-12 my-input">
                                <button class="btn btn-success" @click="registration">Отправить</button>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data () {
            return {
                login: '',
                password: '',
                login_reg: '',
                password_reg: '',
            }
        },
        methods: {
            authorization () {
                if(this.validate(this.login, this.password)) {
                    axios.post('/api/authorization', {login: this.login, password: this.password}).then(response => {
                        this.$router.push({name: 'profile', params: {profile: response.data}})
                    }).catch(response => {
                        alert('Неправильные данные')
                    })
                }
            },
            registration () {
                if(this.validate(this.login_reg, this.password_reg)) {
                    axios.post('/api/registration', {login: this.login_reg, password: this.password_reg}).then(response => {
                        this.login_reg = ''
                        this.password_reg = ''
                        alert('Пользователь создан. Вы можете войти')
                    }).catch(response => {
                        alert('Пользователь уже создан')
                    })
                }
            },
            validate (login, password) {
                if (login.length < 4) {
                    alert('Логин должен быть больше 3-ех символов')
                    return false
                }
                if (password.length < 8) {
                    alert('Пароль должен быть более 8 символов')
                    return false
                }
                return true
            }
        }
    }
</script>

<style scoped>

    .border {
        border: solid 1px;
        padding: 12px
    }

    .my-input {
        margin-top: 10px
    }

</style>