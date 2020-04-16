import React from 'react';
import { Switch, Route } from 'react-router-dom';
import login from './components/login';

const Router = () => {
	return(
			<Switch>
				<Route exact path='/' component={login} />
			</Switch>
		);
}

export default Router;