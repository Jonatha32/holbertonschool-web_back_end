import singUpUser from './4-user-promise';
import uploadPhoto from './5-photo-promise';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const prom = [
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ];

  return Promise.allSettled(prom)
    .then((results) => {
      return results.map((result) => ({
        status: result.status,
        value: result.status === 'fulfilled' ? result.value : result.reason,
      }));
    });
}
