import React, { Component } from 'react';
import withFirebaseAuth from 'react-with-firebase-auth';
import * as firebase from 'firebase/app';
import 'firebase/auth';
import firebaseConfig from './firebase';

const firebaseApp = firebase.initializeApp(firebaseConfig);

class Login extends Component {
	render() {
		const { user, signOut, signInWithGoogle } = this.props;
		return (
			<div>
				{
					user ?
					<p>	hello, {user.displayName}</p>
					: <p>Please sign in</p>
				}
				{
					user
						? <button onClick={signOut}>Out</button>
						: <button onClick={signInWithGoogle}>In Google</button>
				}
			</div>
		);
	}
}
const firebaseAppAuth = firebaseApp.auth();

const providers = {
	googleProvider : new firebase.auth.GoogleAuthProvider(),
};

export default withFirebaseAuth({
	providers,
	firebaseAppAuth,
})(Login);
