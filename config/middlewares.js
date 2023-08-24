module.exports = [
  'strapi::errors',
  'strapi::security',
  'strapi::poweredBy',
  'strapi::cors',
  {
    name: 'strapi::cors',
    config: {
      origin: '*'
    },
  },
  'strapi::logger',
  'strapi::query',
  'strapi::body',
  'strapi::session',
  'strapi::favicon',
  'strapi::public',
];
