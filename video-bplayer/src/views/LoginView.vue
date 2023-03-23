<template>
  <section class="login-main-wrapper">
    <div class="container-fluid pl-0 pr-0">
      <div class="row no-gutters">
        <div class="col-md-5 p-5 bg-white full-height">
          <div class="login-main-left">
            <div class="text-center mb-5 login-main-left-header pt-4">
              <img src="@/assets/img/favicon.png" class="img-fluid" alt="LOGO">
              <h5 class="mt-3 mb-3">Вход</h5>
            </div>
            <form>
              <div class="form-group">
                <label for="login">Telegram логин</label>
                <input id="login" v-model.trim="v$.login.$model" type="text" class="form-control" placeholder="telegram логин">
                <span class='error-field'
                  v-for="error in v$.login.$errors"
                  :key="error" >
                  {{ getError(`${error.$propertyPath}.${error.$validator}`) }}
                </span>
              </div>
              <div class="form-group">
                <label for="password">Пароль</label>
                <input id="password" v-model.trim="v$.password.$model" type="password" class="form-control" placeholder="Пароль">
                <span class='error-field'
                  v-for="error in v$.password.$errors"
                  :key="error" >
                  {{ getError(`${error.$propertyPath}.${error.$validator}`) }}
                </span>
              </div>
              <div class="mt-4">
                <div class="row">
                  <div class="col-12">
                    <span class='error-field'
                      v-for="error in serverErrors"
                      :key="error" >
                      {{ getError(error) }}
                    </span>
                    <button :disabled="v$.$invalid || isLoading" type="button" class="btn btn-outline-primary btn-block btn-lg" v-on:click="signIn">Войти
                    </button>
                  </div>
                </div>
              </div>
            </form>
            <div class="text-center mt-5">
              <p class="light-gray">Нет аккаунта? <a href="/register">Регистрация</a></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import LoginRequest from '@/models/LoginRequest';
import { login } from '@/services/api-service';
import { useStore } from 'vuex';
import { required, minLength } from '@vuelidate/validators';
import useVuelidate from '@vuelidate/core';

@Options({
  components: {},
  validations: {
    login: {
      required,
      minLength: minLength(3),
    },
    password: {
      required,
      minLength: minLength(8),
    },
  },
})
export default class LoginView extends Vue {
  isLoading = false;

  serverErrors: string[] = [];

  login = '';

  password = '';

  v$ = useVuelidate();

  store = useStore();

  errors: { [key: string]: string } = {
    'login.required': 'Обязательное поле',
    'password.required': 'Обязательное поле',
    'login.minLength': 'Минимальная длина 3 символа',
    'password.minLength': 'Минимальная длина 8 символов',
    'user not found': 'Пользователь не найден',
    'wrong password': 'Неверный пароль',
  };

  getError(errorKey: string): string {
    return this.errors[errorKey];
  }

  async signIn(): Promise<void> {
    const loginRequest: LoginRequest = {
      login: this.login,
      password: this.password,
    };

    try {
      this.isLoading = true;
      this.serverErrors = [];
      const user = await login(loginRequest);
      if (user) {
        console.log(user);

        this.store.commit('setUser', user);
        this.$router.push({ name: 'home' });
      }
    } catch (ex: any) {
      if (ex) {
        this.serverErrors.push(ex.message);
      }
    } finally {
      this.isLoading = false;
    }
  }
}
</script>

<style scoped>

</style>
