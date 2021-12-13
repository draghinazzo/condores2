
import Vue from 'vue'
import Router from 'vue-router'
import auth from "@/auth/auth";

import 'firebase/auth'

Vue.use(Router)

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    scrollBehavior() {
      return { x: 0, y: 0 }
    },
    routes: [
      ...auth,
      {
        path: '/login',
        name: 'login',
        component: () => import('@/views/pages/login/Login.vue'),
        meta: {
          requiresAuth: false,
          rule: 'editor'
        }
      },
      {
        path: '/error-404',
        name: 'error-404',
        component: () => import('@/views/pages/Error404.vue'),
        meta: {
        requiresAuth: false,
        rule: 'editor'
        }
      },
      {
        path: '*',
        redirect: 'error-404',
      },
    ],
  })


  router.beforeEach((to, from, next) => {
    const authUser = JSON.parse(window.localStorage.getItem('plataforma-condores'))
    console.log('authUser', authUser)
    // Skip login
    if (!to.meta.requiresAuth) {
      if (authUser && authUser.authentication.isAuthenticated && to.name === 'login') {
        console.log('en el iffffff')
        return next({ name: 'Medio' })
      }
      return next()
    }
  
    if (
      !authUser
      || !authUser.authentication.isAuthenticated
    ) {
      // Login Page
      return next({ name: 'login' })
    }
  
    return next()
  })

export default router
