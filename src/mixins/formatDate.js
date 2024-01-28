export default {
    methods: {
      formatDate(dateString) {
        const releasedate = new Date(dateString);
        const options = { year: 'numeric', month: 'short', day: 'numeric' };
        return releasedate.toLocaleDateString(undefined, options);
      },
    },
  };
  