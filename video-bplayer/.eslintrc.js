module.exports = {
  root: false,
  env: {
    node: false,
  },
  extends: [
    'plugin:vue/vue3-essential',
    '@vue/airbnb',
    '@vue/typescript/recommended',
  ],
  parserOptions: {
    ecmaVersion: 2020,
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'global-require': 'off',
    'no-restricted-syntax': 'off',
    'no-plusplus': 'off',
    'max-len': 'off',
    'class-methods-use-this': 'off',
    'no-trailing-spaces': 'off',
    'vuejs-accessibility/anchor-has-content': 'off',
    'vuejs-accessibility/form-control-has-label': 'off',
    'vuejs-accessibility/media-has-caption': 'off',
    "import/no-extraneous-dependencies": "off",
    "no-underscore-dangle": "off",
    'import/no-dynamic-require': 'off',
    'no-undef': 'off',
    '@typescript-eslint/no-var-requires': 'off',
  },
  overrides: [
    {
      files: [
        '**/__tests__/*.{j,t}s?(x)',
        '**/tests/unit/**/*.spec.{j,t}s?(x)',
      ],
      env: {
        jest: true,
      },
    },
  ],
};
