import fastify from 'fastify';

const app = fastify({ logger: true });

app.get('/', () => {
	return { hello: 'world' };
});

app
	.listen({ port: 3333 })
	.then(() => console.log('App running in port 3333'))
	.catch((err) => {
		app.log.error(err);
	});
